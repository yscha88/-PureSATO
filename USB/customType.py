from enum import Enum


class UnmanagedType(Enum):
    #
    # 요약:
    #     A 4-byte Boolean value (true != 0, false = 0). This is the Win32 BOOL type.
    Bool = 2,
    #
    # 요약:
    #     A 1-byte signed integer. You can use this member to transform a Boolean value
    #     into a 1-byte, C-style bool (true = 1, false = 0).
    I1 = 3,
    #
    # 요약:
    #     A 1-byte unsigned integer.
    U1 = 4,
    #
    # 요약:
    #     A 2-byte signed integer.
    I2 = 5,
    #
    # 요약:
    #     A 2-byte unsigned integer.
    U2 = 6,
    #
    # 요약:
    #     A 4-byte signed integer.
    I4 = 7,
    #
    # 요약:
    #     A 4-byte unsigned integer.
    U4 = 8,
    #
    # 요약:
    #     An 8-byte signed integer.
    I8 = 9,
    #
    # 요약:
    #     An 8-byte unsigned integer.
    U8 = 10,
    #
    # 요약:
    #     A 4-byte floating-point number.
    R4 = 11,
    #
    # 요약:
    #     An 8-byte floating-point number.
    R8 = 12,
    #
    # 요약:
    #     A currency type. Used on a System.Decimal to marshal the decimal value as a COM
    #     currency type instead of as a Decimal.
    Currency = 15,
    #
    # 요약:
    #     A Unicode character string that is a length-prefixed double byte. You can use
    #     this member, which is the default string in COM, on the System.String data type.
    BStr = 19,
    #
    # 요약:
    #     A single byte, null-terminated ANSI character string. You can use this member
    #     on the System.String and System.Text.StringBuilder data types.
    LPStr = 20,
    #
    # 요약:
    #     A 2-byte, null-terminated Unicode character string. You cannot use the LPWStr
    #     value with an unmanaged string unless the string was created by using the unmanaged
    #     CoTaskMemAlloc function.
    LPWStr = 21,
    #
    # 요약:
    #     A Unicode character string. This value is supported only for platform invoke
    #     and not for COM interop, because exporting a string of type LPTStr is not supported.
    LPTStr = 22,
    #
    # 요약:
    #     Used for in-line, fixed-length character arrays that appear within a structure.
    #     ByValTStr types behave like C-style, fixed-size strings inside a structure (for
    #     example, char s[5]). The character type used with ByValTStr is determined by
    #     the System.Runtime.InteropServices.CharSet argument of the System.Runtime.InteropServices.StructLayoutAttribute
    #     attribute applied to the containing structure. Always use the System.Runtime.InteropServices.MarshalAsAttribute.SizeConst
    #     field to indicate the size of the array.
    ByValTStr = 23,
    #
    # 요약:
    #     A COM IUnknown pointer. You can use this member on the System.Object data type.
    IUnknown = 25,
    #
    # 요약:
    #     A COM IDispatch pointer (Object in Microsoft Visual Basic 6.0).
    IDispatch = 26,
    #
    # 요약:
    #     A VARIANT, which is used to marshal managed formatted classes and value types.
    Struct = 27,
    #
    # 요약:
    #     A COM interface pointer. The System.Guid of the interface is obtained from the
    #     class metadata. Use this member to specify the exact interface type or the default
    #     interface type if you apply it to a class. This member produces the same behavior
    #     as System.Runtime.InteropServices.UnmanagedType.IUnknown when you apply it to
    #     the System.Object data type.
    Interface = 28,
    #
    # 요약:
    #     A SafeArray, which is a self-describing array that carries the type, rank, and
    #     bounds of the associated array data. You can use this member with the System.Runtime.InteropServices.MarshalAsAttribute.SafeArraySubType
    #     field to override the default element type.
    SafeArray = 29,
    #
    # 요약:
    #     When the System.Runtime.InteropServices.MarshalAsAttribute.Value property is
    #     set to ByValArray, the System.Runtime.InteropServices.MarshalAsAttribute.SizeConst
    #     field must be set to indicate the number of elements in the array. The System.Runtime.InteropServices.MarshalAsAttribute.ArraySubType
    #     field can optionally contain the System.Runtime.InteropServices.UnmanagedType
    #     of the array elements when it is necessary to differentiate among string types.
    #     You can use this System.Runtime.InteropServices.UnmanagedType only on an array
    #     that whose elements appear as fields in a structure.
    ByValArray = 30,
    #
    # 요약:
    #     A platform-dependent, signed integer: 4 bytes on 32-bit Windows, 8 bytes on 64-bit
    #     Windows.
    SysInt = 31,
    #
    # 요약:
    #     A platform-dependent, unsigned integer: 4 bytes on 32-bit Windows, 8 bytes on
    #     64-bit Windows.
    SysUInt = 32,
    #
    # 요약:
    #     A value that enables Visual Basic to change a string in unmanaged code and have
    #     the results reflected in managed code. This value is only supported for platform
    #     invoke.
    VBByRefStr = 34,
    #
    # 요약:
    #     An ANSI character string that is a length-prefixed single byte. You can use this
    #     member on the System.String data type.
    AnsiBStr = 35,
    #
    # 요약:
    #     A length-prefixed, Unicode char string. You rarely use this BSTR-like member.
    TBStr = 36,
    #
    # 요약:
    #     A 2-byte, OLE-defined VARIANT_BOOL type (true = -1, false = 0).
    VariantBool = 37,
    #
    # 요약:
    #     An integer that can be used as a C-style function pointer. You can use this member
    #     on a System.Delegate data type or on a type that inherits from a System.Delegate.
    FunctionPtr = 38,
    #
    # 요약:
    #     A dynamic type that determines the type of an object at run time and marshals
    #     the object as that type. This member is valid for platform invoke methods only.
    AsAny = 40,
    #
    # 요약:
    #     A pointer to the first element of a C-style array. When marshaling from managed
    #     to unmanaged code, the length of the array is determined by the length of the
    #     managed array. When marshaling from unmanaged to managed code, the length of
    #     the array is determined from the System.Runtime.InteropServices.MarshalAsAttribute.SizeConst
    #     and System.Runtime.InteropServices.MarshalAsAttribute.SizeParamIndex fields,
    #     optionally followed by the unmanaged type of the elements within the array when
    #     it is necessary to differentiate among string types.
    LPArray = 42,
    #
    # 요약:
    #     A pointer to a C-style structure that you use to marshal managed formatted classes.
    #     This member is valid for platform invoke methods only.
    LPStruct = 43,
    #
    # 요약:
    #     Specifies the custom marshaler class when used with the System.Runtime.InteropServices.MarshalAsAttribute.MarshalType
    #     or System.Runtime.InteropServices.MarshalAsAttribute.MarshalTypeRef field. The
    #     System.Runtime.InteropServices.MarshalAsAttribute.MarshalCookie field can be
    #     used to pass additional information to the custom marshaler. You can use this
    #     member on any reference type. This member is valid for parameters and return
    #     values only. It cannot be used on fields.
    CustomMarshaler = 44,
    #
    # 요약:
    #     A native type that is associated with an System.Runtime.InteropServices.UnmanagedType.I4
    #     or an System.Runtime.InteropServices.UnmanagedType.U4 and that causes the parameter
    #     to be exported as an HRESULT in the exported type library.
    Error = 45,
    #
    # 요약:
    #     A Windows Runtime interface pointer. You can use this member on the System.Object
    #     data type.
    IInspectable = 46,
    #
    # 요약:
    #     A Windows Runtime string. You can use this member on the System.String data type.
    HString = 47,
    #
    # 요약:
    #     A pointer to a UTF-8 encoded string.
    LPUTF8Str = 48

